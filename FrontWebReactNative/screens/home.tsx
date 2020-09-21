import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import globalStyles from '../styles/globalStyles'
import RegisterTeam from './screens/RegisterTeam';

const onPress = () => {};

export default function Home ({ navigation }) {
    return (
        <View style={globalStyles.container}>

            <TouchableOpacity
                onPress={() => navigation.navigate('RegisterTeam')}
                style={globalStyles.link}>
                <View >
                    <Text>Crea tu equipo</Text>
                </View>
            </TouchableOpacity>
        </View>
    );

};
