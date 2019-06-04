var React = require('react');
var Text = require('react-native').Text;
var View = require('react-native').View;
var Button = require('react-native').Button;
var AppRegistry = require('react-native').AppRegistry;

const geraNumeroAleatorio = () => {
		var numero_aleatorio = Math.random();
		numero_aleatorio = Math.floor(numero_aleatorio * 10);
		alert(numero_aleatorio);
};

const App = () => {
   return (
       <View>
        <Text>Gerador de números randômicos!!!</Text>
        <Button 
        	title="Gerar um número randômico"
					onPress={geraNumeroAleatorio} 
        />
       </View>
   ); 
};

AppRegistry.registerComponent('app1', () => App);

export default App;
