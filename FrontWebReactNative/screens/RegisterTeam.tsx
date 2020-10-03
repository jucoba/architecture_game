import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles';
import { register_team_api_call } from '../ApiCalls/register_server_api';


function register_team ( team_name, player_name, navigation) {

    let response = register_team_api_call( team_name, player_name);
    response.then(
        function(value) {
            navigation.navigate('TeamPanel', {value })
        }
    )

};


function RegisterTeam ( {navigation}) {
    return  ( <RegisterTeam_with_function onSubmit = { register_team }  navigation = {navigation} />);

};

function RegisterTeam_with_function ( {onSubmit, navigation} ) {

    const [team_name_input, setTeam_name_input] = useState('');
    const [player_name_input, setPlayer_name_input] = useState('');

    return (
        <View style={globalStyles.container}>
            <Text style={globalStyles.text}>Nombre de tu equipo</Text>
            <TextInput style={globalStyles.textInupt}
                accessibilityLabel="team-name"
                onChangeText = {text => setTeam_name_input(text) }
                testID="register_team_text_input"
            />
            <TouchableOpacity onPress= { () => onSubmit(team_name_input, player_name_input, navigation)  } >
                <Text>Crea tu equipo</Text>
            </TouchableOpacity>
        </View>
    );

};


export default RegisterTeam;
export { RegisterTeam, RegisterTeam_with_function };



