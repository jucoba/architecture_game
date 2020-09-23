import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles'

const register_team = () => {
    return fetch('/register_team')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
      console.error(error);
    });
};

export default function RegisterTeam () {
    return (
        <View style={globalStyles.container}>
            <Text style={globalStyles.text}>Nombre de tu equipo </Text>
            <TextInput style={globalStyles.textInupt}/>
            <Text style={globalStyles.text}>Tu Nombre </Text>
            <TextInput style={globalStyles.textInupt}/>
            <TouchableOpacity onPress={register_team} style={globalStyles.button}>
                <View >
                    <Text>Crea tu equipo</Text>
                </View>
            </TouchableOpacity>
        </View>
    );

};

