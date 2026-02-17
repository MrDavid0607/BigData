from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(math.isqrt(n))
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        valor = input("Ingresa un número: ").strip()
        n = int(valor)

        if es_primo(n):
            print(f"{n} es primo ✅")
        else:
            print(f"{n} NO es primo ❌")

    except ValueError:
        print("Error: debes ingresar un número entero.")
