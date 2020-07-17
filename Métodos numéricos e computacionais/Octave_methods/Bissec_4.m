f = input("Entre com a fun��o f(x): ");
A = input("Entre com o limite inferior A: ");
B = input("Entre com o limite superior B: ");
e = input("Entre com o erro m�ximo permitido: ");

bissec_4(f, A, B, e)

#Defini��o da fun��o que encontra as raizes reais da fun��o
function bissec_4(f, A, B, e)

  #Valor de A e B na funcao
  fA = f(A);
  fB = f(B);

  i = 0;
  if fA*fB > 0
    fprintf("N�o existe raiz no intervalo [%f,%f] ou o intervalo � muito grande", A, B);
  else
    
    #Defini��o do intervalo para parada posterior  
    int = abs(B-A);

    #Ponto M�dio
    Pm = (A+B)/2;

    while int > e 

      if f(Pm) == 0  
        break;
      endif
      
      #Condi��es de zero em um intervalo 
      if f(A) * f(Pm) > 0 
        A = Pm;  
      else
        B = Pm;
      endif   
      Pm = (B+A)/2;
      
      i++;
      fprintf("Itera��o %i com fPm = %f\n", i, f(Pm));
      int = abs(B-A);
    endwhile
    
    fprintf("O zero da equa��o esta pr�ximo do ponto x=%f onde f(%f)=%f", Pm, Pm, f(Pm));
  endif

endfunction