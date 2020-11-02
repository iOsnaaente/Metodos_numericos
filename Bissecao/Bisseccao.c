/*
Aula Pr�tica 1 - Introdu��o � Programa��o

Implemente um algoritmo descrito em linguagem C (preferencialmente) ou Java com o m�todo num�rico de busca por raiz de fun��o por bisse��o  que:

Permita a escolha da se��o inicial (pontos A e B)
Fa�a o teste para saber se A e B dados s�o v�lidos para intervalo da raiz
Permita configura��o da toler�ncia ou se��o m�nima
Mostre os valores de cada itera��o
Mostre o valor encontrado para a raiz com o n�mero de itera��es e o erro
Dados os as seguintes informa��es:

Fun��o: f(x) = x3/10 + x2/2 - 3x + 10

*/

// COMPILADOR -> MinGW32 - gcc

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale.h>

// Fun��o: f(x) = x^3/10 + x^2/2 - 3x + 10
double apply(double x){
    return  ((pow(x,3)/10) + (pow(x,2)/2) - 3*x + 10);
}

int main(){
    // Permiss�o da lingua portuguesa (acentos)
    setlocale(LC_ALL, "portuguese");

    // Declara��o dos Pontos A e B
    double Pa, Pb;

    // Itera��o e Se��o m�nima
    int i = 0;
    double secMin = 0.0000001;


    printf("C�digo de Bisse��o de uma fun��o f(x)\n");
    printf("Fun��o-> f(x) = x^3 / 10 + x^2 / 2 - 3x + 10 \n\n");

    printf("D� entrada aos valores limites de A (inferior) e B (Superior):\n " );

    // %lf -> long float = double
    scanf("%lf", &Pa);
    scanf("%lf", &Pb);


    // Aplica��o dos pontos Pa e Pb em F(x)
    double FxA = apply(Pa);
    double FxB = apply(Pb);
    double Pm = (Pa + Pb)/2;
    double Fm = apply(Pm);
    double raiz;

    printf("Os valores de limites s�o (%2.4lf, %2.4lf) -> (%2.4lf, %2.4lf)\n\n", Pa, Pb, FxA, FxB);

    do{

        FxA = apply(Pa);
        FxB = apply(Pb);
        Fm  = apply(Pm);

        raiz = Pm;

        printf("Itera��o %i \t", i);
        printf("Os valores de (%2.4lf, %2.4lf) -> (%2.4lf, %2.4lf) \t", Pa, Pb, FxA, FxB);
        printf("A raiz mais pr�xima �: %2.4lf\n", raiz);

        if (FxA * FxB > 0){
            printf("\nIntervalo inv�lido para analise da bissec��o, duas raizes entre (%2.4lf , %2.4lf)", Pa, Pb);
            return 0;

        } else if (FxA == 0){
            raiz = Pa;
            break;
        }else if (FxB == 0){
            raiz = Pb;
            break;
        }else{
            if (FxA*Fm > 0)     Pa = Pm;
            else                Pb = Pm;
        }
            Pm = (Pa+Pb)/2;

        printf("--------------------------------------------------------------------------------\n");
        i++;

    }while((Pb-Pa) > secMin);

        printf("\n\n");
        printf("Itera��o %i \t", i);
        printf("Os valores de (%2.8lf, %2.8lf) -> (%2.8lf, %2.8lf) \t", Pa, Pb, FxA, FxB);
        printf("\n\nA raiz mais pr�xima �:  %2.10lf \n\n", Pm);

    return 0;
}
