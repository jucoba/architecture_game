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

    return (

        <View style={globalStyles.mainContainer}>

            <View style={globalStyles.titleContainer}>
                <Text style={globalStyles.titleText}>{json_team.team_name}</Text>
                <View style={globalStyles.fixedProperty}>
                    <Text >Saldo </Text>
                    <Text >{json_team.balance}</Text>
                </View>
            </View>
            <View style={globalStyles.properyContainer}>
                <Text style={globalStyles.propTitle}>Nivel de arquitectura</Text>
                <Text >
                    {json_team.architecture_level}
                </Text>
            </View>
            <View style={globalStyles.clientsContainer}>
                <View style={globalStyles.properyContainer}>
                    <Text style={globalStyles.propTitle}>Número de Clientes</Text>
                    <Text>{json_team.current_clients}</Text>
                </View>
                <View style={globalStyles.properyContainer}>
                    <Text style={globalStyles.propTitle}>Capacidad máxima de Clientes</Text>
                    <Text>{json_team.capacity}</Text>
                </View>
            </View>
            <View style={globalStyles.pnlContainer}>
                <View style={globalStyles.properyContainer}>
                    <Text style={globalStyles.propTitle}>Ingresos</Text>
                    <Text>{json_team.income}</Text>
                </View>
                <View style={globalStyles.properyContainer}>
                    <Text style={globalStyles.propTitle}>Costos</Text>
                    <Text>{json_team.cicle_cost}</Text>
                </View>
                <View style={globalStyles.properyContainer}>
                    <Text style={globalStyles.propTitle}>PyG</Text>
                    <Text>{json_team.pyg}</Text>
                </View>
            </View>


        </View>

    );
};