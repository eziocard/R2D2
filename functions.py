
import torch
from torch.optim import AdamW
from transformers import AutoTokenizer,AutoModelForSequenceClassification
from pathlib import Path
from resolver import manejar_proyecto
MODEL_DIR = Path(__file__).resolve().parent / "modelo"

def load_model(model_base):
    print(f'Descargando modelo {model_base}')
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_base)
       
    except ValueError as e:
        print(f'Error al descargar modelo {model_base}')
        print(f'Error: {e}')
        return None

    return tokenizer

def load_trained_model():
    if not MODEL_DIR.exists():
        return None, None

    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

        return model, tokenizer

    except Exception as e:
        print(f"Error al cargar el modelo entrenado: {e}")
        return None, None


def prepare_data(train_dataset,tokenizer):
    phrases = [item[0] for item in train_dataset]
    labels = [item[1] for item in train_dataset]
    
    inputs = tokenizer(phrases,padding=True,truncation=True,return_tensors="pt")
    labels = torch.tensor(labels)

    return labels,inputs


def fine_tuning(model_base, categories, epochs, inputs, labels):
    try:
        model = AutoModelForSequenceClassification.from_pretrained(
            model_base,
            num_labels=len(categories)
        )
    except (ValueError, OSError) as e:
        print('Error al cargar modelo')
        print(f'Error: {e}')
        return None

    optimizer = AdamW(model.parameters(), lr=2e-5)
    print("\n Iniciando Fine-tuning")
    model.train()

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(**inputs, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f" Época {epoch+1}/{epochs} | Error (Loss): {loss.item():.4f}")

    print('\nEntrenamiento terminado\n')
    MODEL_DIR.mkdir(exist_ok=True)
    model.save_pretrained(MODEL_DIR)
    return model

def infer(model, tokenizer, categories, answers):
    model.eval()

    while True:
        phrase_user = input("\n>[R2D2] Ingresa un texto: ")

        if phrase_user.lower() in [
            "salir",
            "exit",
            "quit"
        ]:
            print("[R2D2]: Hasta luego")
            break

        inputs_user = tokenizer(
            phrase_user,
            padding=True,
            truncation=True,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = model(**inputs_user)

            logits = outputs.logits

            probabilities = (
                torch.nn.functional.softmax(
                    logits,
                    dim=-1
                )[0]
            )

            index_winner = torch.argmax(
                probabilities
            ).item()

            level_confidence = (
                probabilities[index_winner].item()
                * 100
            )

            predicted_category = (
                categories[index_winner]
            )

            #print(
            #    f" [R2D2 DETECTA]: "
            #    f"Intención -> "
            #   f"'{predicted_category}' "
            #    f"| Confianza -> "
            #    f"{level_confidence:.1f}%"
            #)

            if level_confidence < 45:
                print(
                    "[R2D2]: "
                    "No estoy seguro de haber "
                    "entendido. ¿Puedes "
                    "reformularlo?"
                )
                continue

            print(
                f"[R2D2]: "
                f"{answers.get(predicted_category)}"
            )

            if predicted_category in ["ABRIR_PROYECTO", "CREAR_PROYECTO", "LISTAR_PROYECTOS"]:
                manejar_proyecto(predicted_category, phrase_user)
