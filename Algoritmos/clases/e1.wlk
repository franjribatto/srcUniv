object pepita {
  var energia = 100
  
  method energiaGetter() {
    energia
  }
  
  method volar() {
    energia -= 10
  }
  
  //Setter
  method comer(cantidad) {
    energia += 2 * cantidad
  }
}