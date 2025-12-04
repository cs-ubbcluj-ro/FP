Layered Architecture

**What is it?**

- It is a design pattern (a way to organize code) for writing large programs
- The program is made up of layers
    - Each layer has access to classes in its own layer, or the layer immediately below
- What layers are there usually?
    1. Presentation layer (at the top, user interface)
        - All the user interaction (reading data, presenting data to the user, presenting error information etc.)
        - Classes like _BakeryUI_
        - This layer talks only with the service layer
    2. Service layer (or controller layer)
       - Each entity in the domain should have its own service class
       - Classes like _RecipeService_, _ProductService_ etc.
       - No user input/output here, just parameters and raising exceptions
       - Talks only with the data persistence layer
    3. Data persistence layer (or repository layer)
       - Its job is to persist the entitites in the problem domain
       - Might use memory (v1), binary/text files (v2), databases (SQL/noSQL) (v3)
    4. Domain
        - The domain contains the classes from the problem domain (e.g., _Product_, _Recipe_, _Ingredient_, etc.)
        - Classes from the domain do not know about any other layer
        - All other layer can use classes from the domain