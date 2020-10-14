
import React from "react";
import { StyleSheet } from 'react-native';


const globalStyles = StyleSheet.create({
    mainContainer: {
        flexDirection: 'column',
        backgroundColor: '#fff',
    },
    titleContainer: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#fff',
        alignItems: 'center'
    },
    clientsContainer: {
        flexDirection: 'column',
        backgroundColor: '#b3e5fc',
        justifyContent: 'flex-start',
        alignItems: 'flex-start',
        margin:15,
        width: 300,

    },
    pnlContainer: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#4fc3f7',
        justifyContent: 'flex-start',
        margin:15,
        width: 300,

    },
    properyContainer: {
        flexDirection: 'row',
        justifyContent: 'flex-start',
    },
    propTitle: {
        marginEnd:5,
        fontWeight: 'bold'
    },
    fixedProperty: {
        flex: 1,
        flexDirection: 'row',
        backgroundColor: '#fff',
        alignItems: 'flex-start'
    },
    titleText: {
        fontSize:30,
    },
    textInupt: {
        borderColor: 'gray',
        borderWidth: 1,
        margin:5,
    },
    text: {
        margin:5,
    },

    button: {
        margin:5,
        alignItems: "center",
        backgroundColor: "#DDDDDD",
        padding: 10
    },
    link: {
        margin:5,
        padding: 10
    },
}
);

export default globalStyles