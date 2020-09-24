import { render, fireEvent } from '@testing-library/react-native';
import React from 'react';
import RegisterTeam   from '../screens/RegisterTeam';

test('Register team shoud have two texts and one button', () => {
    console.log (RegisterTeam)
    const { getAllByA11yLabel, getByText }  = render( <RegisterTeam /> );

    const team_name_input = getAllByA11yLabel('team-name');
    expect(team_name_input).toBeDefined();

    const player_name_input = getAllByA11yLabel('player-name');
    expect(player_name_input).toBeDefined();

    const submit_button = getByText('Crea tu equipo');
    expect(submit_button).toBeDefined();
});