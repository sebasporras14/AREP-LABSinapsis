# Taller Sainapsis

## Planteamiento 
El objetivo de este taller es aprender a utilizar Langchain (herramienta fundamental para crear agentes que usen la técnica de Retrieval Augmented Generation, también llamada RAG) además de evaluar buenas prácticas y clean code de Python.  

Las siguientes tareas y desafíos le ayudarán a afianzar el conocimiento en los campos mencionados anteriormente.  

El objetivo final es la creación de un API REST que acepte por input un mensaje de usuario final (para ser procesado por orquestador (api de python que corra un agente de [Langchain](https://python.langchain.com/docs/get_started/introduction)) y utilizando una base de datos de vectores y los endpoints de OpenAI para su LLM, genere una respuesta.


## Desafío #1
Crear una base de datos de vectores en [Pinecone Starter Version](https://www.pinecone.io/) usando su correo institucional, cargar los documentos anexos (FAQs de universidades) usando Embeddings de OpenAI y Langchain. Configurar una Tool de langchain que consulte los documentos y genere una respuesta.

## Prerequisitos:
Es necesario tener instaladas las siguientes librerías en nuestros entornos de trabajo(en el proyecto ya se encuentran en el archivo de requirements):
```
pip install ChatOpenAI
pip install AgentType
pip install initialize_agent
pip install tool
pip install OpenAIEmbeddings
pip install Pinecone
```

## Desarrollo
Primero, configuramos la API key de OpenAI en Windows como variable de entorno brindada en la clase y solo para uso en esta:
```
OPENAI_API_KEY = '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'
```
replicamos el agente básico que se nos presentó, haciendo uso de Langchain: Agents, Tools, Embeddings y Vectorstores - Pinecone  
![imagen](https://github.com/sebasporras14/AREP-LABSinapsis/assets/69282634/5f84ba97-2e58-4050-afd5-302f18890ef7)

luego añadiremos los documentos con información de los diferentes programas en la ECI encontrados en la carpeta de documentos:
![imagen](https://github.com/sebasporras14/AREP-LABSinapsis/assets/69282634/189dafb0-6d22-46a5-a068-ec76a1affcfe)
Creamos una base de datos de Vectores en Pinecone, ingresando con nuestra cuenta institucional:
![imagen](https://github.com/sebasporras14/AREP-LABSinapsis/assets/69282634/59728e7e-dc63-4a3c-bcdb-1f086da11b1b)
Configuramos la API key de Pinecone y el environment en Windows como variables de entorno:
Vectorizamos estos documentos y los subimos a la base de Datos recién creada:
   ![imagen](https://github.com/sebasporras14/AREP-LABSinapsis/assets/69282634/a9781763-238f-44bb-a08c-8dc0dd13986b)
   ![imagen](https://github.com/sebasporras14/AREP-LABSinapsis/assets/69282634/95c332fd-cb1f-4ac5-b63e-2134f2605abc)
Creamos un método de búsqueda con OpenAI, Pinecone y sus agentes, en búsqueda de implementar un nuevo tool:

   ![imagen](https://github.com/sebasporras14/AREP-LABSinapsis/assets/69282634/559fcc9e-9b67-4189-ae45-bc2a87608587)

   

## Funcionamiento
No se puedo tener evidencias de funcionamiento el dia de la realizacion debido a que apenas finalizo la clase la API Key fue revocada 

## Autor
Sebastian porras
