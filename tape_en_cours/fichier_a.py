print("dans fichier a", f"{__name__=}")
import fichier_b


def f() -> None:
    """TOTO"""
    print("dans f")


if __name__ == "__main__":
    f()
