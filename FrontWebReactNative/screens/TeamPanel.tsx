import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles';
import { get_team_api } from '../ApiCalls/get_team_api';


export default function TeamPanel( {id }) {

    return (  <View style={globalStyles.container}>
                <Text>hola</Text>
              </View> );
};