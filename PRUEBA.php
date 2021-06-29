<?php

require('somefile.php');

 $variable = 9;
 $v1;

 $booleano = true;
 
 echo "esto es un print, se muestra en pantalla";
 echo $verb;
 
 if($a < 20){
  $v1 = 1;
  echo $v1;
  $suma = $v2 + $v3;
}
  
  //~ class ClaseSencilla
//~ {
  //~ public $var = 0;
  //~ public $var1 = 0;
  //~ 
  //~ protected function mostrarVar() {
    //~ return 0;
  //~ }
//~ }

function recursividad($a)
{
  if($a < 20){
    $v1 = 1;
    echo $v1;
    $suma = $v2 + $v3;
  }
  
  echo "esto es un print, se muestra en pantalla";
  
  switch($suma)
  {
    case 1: $v1 = $variable + $v1; break;
    case 3: $v2 = $variable + $v2; break;
    case 4: $v3 = $variable; break;
    default: $v4 = $variable; break;
  }
  
  while($j<=$i)
  {
    echo "*&nbsp&nbsp";
  }
  
}

class ClaseSencilla
{
    // Declaración de una propiedad
    public $var = 0;
    private $car = 0;

    // Declaración de un método
    public function mostrarVar() {
        echo $this->var;
    }
}
  
//esto es un comentario corto 

/* 
 * esto es un comentario largo deberia 
 * reconocerlo todo por saltos de linea 
 * que haga 
*/

?>
