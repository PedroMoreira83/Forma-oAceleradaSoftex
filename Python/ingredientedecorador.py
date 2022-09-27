class Sanduiche():

    def operation(self) -> str:
        pass
    def custo(self) -> float:
        pass

class FrangoAssado(Sanduiche):

    def operation(self) -> str:
        return "Sanduíche de Frango Assado"

class ingredienteDecorador(Sanduiche):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Sanduiche = None

    def __init__(self, component: Sanduiche) -> None:
        self._component = component

    @property
    def component(self) -> Sanduiche:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Pepperoni(ingredienteDecorador):

    def operation(self) -> str:

        return f" pepperoni({self.component.operation()}) "

   # def custo(self) -> float:


class Bacon(ingredienteDecorador):

    def operation(self) -> str:
        return f" bacon({self.component.operation()})"


#def client_code(component: Sanduiche) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

   # print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = FrangoAssado()
    print(f'Este é o ${FrangoAssado.operation} e seu custo é ${FrangoAssado.custoingredientedecorador}.')
    #client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
   # decorator1 = ConcreteDecoratorA(simple)
   # decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    #client_code(decorator2)