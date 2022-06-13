Testado no python 3.9.5

Por enquanto eu fiz um esquema assim:

[
    {'beat': XXX, 'note': YZ, 'timestamp': W.WW},
    {'beat': XXX, 'note': YZ, 'timestamp': W.WW},
    {...},
    ...
]

Sendo:

XXX: em qual batida a nota acontece
Y: Oitava a que a nota pertence
Z: A nota em si (C=Dó, D=Ré, ....)
W.WW: em quantos segundos da música a nota é tocada, basicamente (BPM / 60 * batida)