import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
from sklearn.metrics import confusion_matrix, recall_score
import matplotlib.pyplot as plt

train_data_dir = 'train'
validation_data_dir = 'vali'

train_datagen = ImageDataGenerator(
		rescale=1./255,
		rotation_range=180,  
		width_shift_range=0.1, 
		height_shift_range=0.1, 
		shear_range=0.01, 
		zoom_range=0.20, 
		horizontal_flip=True,
        vertical_flip=True,
		fill_mode="nearest")

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(512, 512),
        batch_size=32,
        class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(512, 512),
        batch_size=32,
        class_mode='categorical')
        
num_classes = 4

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(512, 512, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(1024, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5)) 
model.add(Dense(num_classes, activation='softmax'))  



model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("treinando o modelo")
hist_Treino = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // train_generator.batch_size,
        epochs=200,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // validation_generator.batch_size)

model.save('modelo_treinadoRNfinal.h5')

##CALCULANDO MATRIZ DE CONFUSAO
y_pred_train = model.predict(train_generator)
y_pred_val = model.predict(validation_generator)

y_pred_train_classes = np.argmax(y_pred_train, axis=1)
y_pred_val_classes = np.argmax(y_pred_val, axis=1)

y_true_train = train_generator.classes
y_true_val = validation_generator.classes

cm_train = confusion_matrix(y_true_train, y_pred_train_classes)
cm_val = confusion_matrix(y_true_val, y_pred_val_classes)

with open("matriz_confusaoProRN.txt", "w") as f:
    f.write("Matriz de Confusão - Treinamento:\n")
    np.savetxt(f, cm_train, fmt="%d")
    f.write("\n\nMatriz de Confusão - Validação:\n")
    np.savetxt(f, cm_val, fmt="%d")
print("Matrizes de Confusão salvas em um único arquivo de texto.")


##CALCULANDO RECALL
recall_values = []
for i in range(num_classes):
    y_true_class = (y_true_val == i)
    y_pred_class = (y_pred_val_classes == i)
    recall = recall_score(y_true_class, y_pred_class)
    recall_values.append(recall)

file_name = "recall_values.txt"

with open(file_name, "w") as f:
    for i, recall in enumerate(recall_values):
        f.write("Recall - Classe {}: {:.4f}\n".format(i, recall))

print("Valores de Recall salvos em {}.".format(file_name))

##ACURACIA TOTAL DO MODELO
test_loss, test_accuracy = model.evaluate(validation_generator)
print("Acurácia total do modelo: {:.2f}%".format(test_accuracy * 100))

##FIGURA PERDA E ACURACIA TREINAMENTO
plt.figure(figsize=(10, 6))
plt.plot(hist_Treino.history['loss'], label='Train Loss')
plt.plot(hist_Treino.history['accuracy'], label='Train Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.title('Training Progress')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('Perda-Acuracia-RN-Final-Treino.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(hist_Treino.history['loss'], label='Train Loss', color='#0066CC')
plt.plot(hist_Treino.history['accuracy'], label='Train Accuracy', color='#FF8000')
plt.plot(hist_Treino.history['val_loss'], label='Validation Loss', color='#3399FF', linestyle='--')
plt.plot(hist_Treino.history['val_accuracy'], label='Validation Accuracy', color='#FFB266', linestyle='--')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.title('Training Progress')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('Perda-Acuracia-RN-Final-TreVal.png')
plt.show()
   
print("Acabou!")
