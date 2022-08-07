## Documentation

This is a solution for the IA python Exam. It was created by Humberto Villegas

## Technologies
- Back-End: Python with Flask
- Front-End: React with Bootstrap
- Storage: Flask SQLite

## Development Setup
### Prerequisites
- Install [Node.js] which includes [Node Package Manager][npm]
- Install [Python] 

### How to run REST API
- Download the repository
- In CMD, locate yourself in the "APIRest" folder
- Write the command to enter to virtual environment:

```
venv\Scripts\activate
```

- Run the application:
```
flask --app iaExam run
```

### How to run FrontEnd
- Download the repository
- In CMD, locate yourself in the "website" folder
- Run the application:
```
npm start
```

### How to run postman collection
- Download the repository
- In Postman, open File -> Import...
- Click on Upload Files
- Select the file "APIRest Collection Humberto"
- Click on Import

[python]: https://www.python.org/
[node.js]: https://nodejs.org/
[npm]: https://www.npmjs.com/get-npm
