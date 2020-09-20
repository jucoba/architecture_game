import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles'

export default function RegisterTeam () {
    return (
        <View style={globalStyles.container}>
            <Text>Nombre de tu equipo </Text>
            <TextInput style={globalStyles.textInupt}/>
            <Text>Tu Nombre </Text>
            <TextInput style={globalStyles.textInupt}/>
            <Button
                title="Crea tu equipo"
            />
        </View>
    );

};

