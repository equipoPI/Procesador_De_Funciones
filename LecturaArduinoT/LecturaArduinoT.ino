/* 
este programa demuestra el uso del las interrupciones generadas por un timer para manejar el 
conversor analógico digital manejando los registros del microcontrolador
*/
#include <TimerOne.h>

#define pulsadorPin 2 // Pin del pulsador de habilitar y desabilitar muestreo
#define LED 13        // Led de control
volatile boolean habilitarADC = true; // Variable para habilitar o deshabilitar el ADC
int result_adc;  //resultado del conversor analógico digital.

void imprime_ADC(void);   //funcion encargada de enviar por el puerto seriel los datos obtenidos
void config_ADC(void);    //función de configuracion del conversor ADC
void config_timer1(void); //funcion de configuración del timer, el cual controla los disparos del ADC

void SPlotter() { // Cambia el estado de habilitarADC cuando se produce una interrupción
  habilitarADC =! habilitarADC;
}

void setup(){
  pinMode(pulsadorPin, INPUT); //defino modo de trabajo de los pines digitales
  pinMode(LED, OUTPUT); 
  attachInterrupt(digitalPinToInterrupt(pulsadorPin), SPlotter, RISING); //defino interrupcion externa para frenar o iniciar el muestreo
  config_ADC();
  cli();
  config_timer1();
  sei();
  Serial.begin(2000000);
}
  
void loop(){
  //La función que detecta si se ha presionado una tecla se ejecuta continuamente
  
}

void config_ADC(void){
  DIDR0 = DIDR2 = 0xFF;   //deshabilito las entradas digitales correspondientes a los canales analógicos
  ADMUX = 0x40;            // 0100 0001 voltaje de ref = 5v, justificación derecha, medida por el canal 0
  ADCSRA = 0xAC;           // 1010 1100 Habilito el conversor ADC, Habilita la interrupcion, INicia el preecalador en 16
  ADCSRB = 0x45;           // 0100 0101 AD channels MUX on, free running mode
  sei();                   // set interrupt flag
  }

void config_timer1(void){
  Timer1.initialize(1000); //establece intervalo de disparo del time
  Timer1.attachInterrupt (timer1_Isr); //establece la funcion asociada al disparo del timer
  TCNT1=0;
  }
 
  /*** Interrupt routine ADC ***/

  
void timer1_Isr() {       //interrupcion del ADC disparada por el timer
  result_adc = ADCL;        // guarda los bytes bajo del ADC
  result_adc += ADCH << 8;  // guarda los bytes altos ADC
  imprime_ADC();
}


void imprime_ADC(void){//solo imprime cuando esta habilitado el conversor
  if(habilitarADC == true){
  digitalWrite(LED, HIGH); //cambia de estado la salida del led
    Serial.println(result_adc);
  }
  else{
    digitalWrite(LED, LOW);
    }
}
