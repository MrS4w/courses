import React from "react";
import { Text, AppRegistry, View } from "react-native";

const Estilos = {
   estiloTexto: {
      fontSize: 40,
      backgroundColor: "#08509B"
   },
   estiloTexto2: {
      fontSize: 40,
      backgroundColor: "#2A48FA"
   },
   estiloView: {
      backgroundColor: "skyblue",
      height: 600,
      // flex-start center flex-end
      justifyContent: "space-around",
      alignItems: "stretch",
      flexDirection: "column"
   }
};

const App = () => {
   const { estiloTexto, estiloTexto2, estiloView } = Estilos;

   return (
      <View style={estiloView}>
         <Text style={estiloTexto}>A</Text>
         <Text style={estiloTexto2}>B</Text>
         <Text style={estiloTexto2}>C</Text>
      </View>
   );
};

AppRegistry.registerComponent("app2", () => App);

export default App;
