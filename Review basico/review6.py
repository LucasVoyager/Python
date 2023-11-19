velocidade = 61;
local_veiculo = 100;
RADAR_1 = 60;
LOCAL_1 = 100;
RADAR_RANGE = 1;
vel_carr_pass_radar_1 = velocidade > RADAR_1;
carro_passou_radar_1 = local_veiculo >= (LOCAL_1 - RADAR_RANGE) and local_veiculo <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carr_pass_radar_1
if vel_carr_pass_radar_1:
    print(f' Velocidade do carro passou do radar')
if carro_passou_radar_1:
    print(f' carro passou no radar')         
if carro_multado_radar_1:
    print(f' carro foi multado pelo radar')
