import { StatusBar } from 'expo-status-bar';
import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles';
import { get_team_api } from '../ApiCalls/get_team_api';



export default function TeamPanel( {route, navigation }) {
    const { value } = route.params;
    const [id, setId] = useState(JSON.stringify(value));

    const [json_team, setJson_team] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(
        () => {
            fetch('http://localhost:5000/team/'+id)
                .then((response) => response.json())
                .then((json) => setJson_team(json) )
                .catch((error) => console.log(error)  )
                .finally( () => setLoading(false) )
        }, [id]
    );

    return (  <View style={globalStyles.container}>
                <Text>hola {id}</Text>
                <TextInput
                    onChangeText = {(text) => setId(text) }
                />
              </View> );
};