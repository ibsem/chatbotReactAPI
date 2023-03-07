# Roteiro para criar uma aplicação chatbot exemplo (front-> react, back-> FastAPI)

############# trocar 127.0.0.1 para localhost quando for desenvolver em windows ###################################

## 1. Para gerenciar as versões do Node
```
nvm ls #lista versoes instaladas do node
```
```
nvm use <node_version> #seta qual versao será utilizada
```
## 2. Para Configurar o ambiente...
```
# Instale o FastAPI Python
pip install Fastapi

# Para inicializar o Backend
uvicorn main:app --reload

# Instale o Expo CLI
npm install -g expo-cli

# Crie um novo projeto React Native
expo init myproject

- cd chatbotReact
- yarn start # you can open iOS, Android, or web from here, or run them directly with the commands below.
- yarn android
- yarn ios
- yarn web

# Instale o axios
npm install axios
```
## 3. Para criar o Backend com FastAPI
```
from fastapi import FastAPI

app = FastAPI()

@app.post('/api/chatbot')
async def chatbot(message: str):
    response = {'message': 'Você disse: ' + message}
    return response
```

## 4. Para criar o Frontend com React Native
```
import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Button, Text } from 'react-native';
import axios from 'axios';

export default function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSendMessage = () => {
    axios.post('http://localhost:8000/api/chatbot', { message })
      .then(res => setResponse(res.data.message))
      .catch(error => console.error(error));
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>ChatBot</Text>
      <TextInput
        style={styles.input}
        placeholder="Digite sua mensagem"
        onChangeText={setMessage}
        value={message}
      />
      <Button title="Enviar" onPress={handleSendMessage} />
      {response ? <Text style={styles.response}>{response}</Text> : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    width: '80%',
    height: 40,
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginBottom: 20,
  },
  response: {
    marginTop: 20,
    fontWeight: 'bold',
  },
});
```

## Referências:
https://daily.dev/blog/how-to-use-multiple-node-versions-with-nvm-on-macos-node-version-manager

https://dev-yakuza.posstree.com/en/react-native/install-on-mac/
