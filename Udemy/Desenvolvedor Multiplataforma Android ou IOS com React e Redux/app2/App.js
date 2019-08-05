import React from "react";
import { Text, AppRegistry, View, Image } from "react-native";

const Estilos = {
   principal: {}
};

const App = () => {
   const { principal } = Estilos;

   return (
      <View style={principal}>
         <Image source={require("./img/uvas.png")} />
         <Text>Legenda para a foto</Text>
      </View>
   );
};

AppRegistry.registerComponent("app2", () => App);

export default App;
