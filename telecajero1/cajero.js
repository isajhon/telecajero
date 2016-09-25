function cambio(){
	
	var cambio =prompt("Ingrese su nueva clave: ", " ");
	alert ("Su cambio de clave fue exitoso, su nueva clave es: "+cambio);
   }
 
function deposito(){
	
		var cuenta=prompt("Ingrese su numero de cuenta: ", " ");
      	var cantidad=prompt("Ingrese el monto a depositar: ", " ");
      	alert ("Su numero de cuenta es: "+cuenta+"\nEl monto depositar es: "+cantidad);
      
     }	
		
function retiro(){
	
		var cedula=prompt("Ingrese su numero de cedula: ", " ");
      	var cuenta=prompt("Indique el tipo de cuenta: Corriente, Ahorro, Maxima: ", " ");
      	var monto=prompt("Ingrese el monto a retirar: ", " ");
      	alert ("Usted portador de la cedula Nº: "+cedula+"\nDesea retirar de la cuenta: "+cuenta+"\nLa cantidad de: "+monto+" Bolivares ");
	
	}

