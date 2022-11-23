print("dans fichier a", f"{__name__=}")


def f() -> None:
    import fichier_b

    """TOTO"""
    print("dans f")


if __name__ == "__main__":
    f()
