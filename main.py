from functions import (
    load_model,
    load_trained_model,
    prepare_data,
    fine_tuning,
    infer,
)

from context import train_dataset, categories, answers

MODELO_BASE = "dccuchile/bert-base-spanish-wwm-uncased"
EPOCHS = 5


def main():
  
    model, tokenizer = load_trained_model()

    if model is None or tokenizer is None:
        print("No existe un modelo entrenado. Entrenando uno nuevo...\n")

        tokenizer = load_model(MODELO_BASE)
        if tokenizer is None:
            print("No se pudo cargar el tokenizador. Abortando.")
            return

        labels, inputs = prepare_data(
            train_dataset,
            tokenizer
        )

        model = fine_tuning(
            MODELO_BASE,
            categories,
            EPOCHS,
            inputs,
            labels
        )

        if model is None:
            print("No se pudo entrenar el modelo. Abortando.")
            return


        tokenizer.save_pretrained("./modelo")

        print("\nModelo entrenado y guardado correctamente.\n")

    else:
        print("Modelo entrenado encontrado. Cargando...\n")

    infer(
        model,
        tokenizer,
        categories,
        answers
    )


if __name__ == "__main__":
    main()