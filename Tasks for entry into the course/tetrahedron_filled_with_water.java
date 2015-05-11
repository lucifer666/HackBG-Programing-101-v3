// задачите са писани в работна среда Eclipse на Java
 
package hackBG;
import java.util.LinkedList;
import java.util.Scanner;
 
public class tetrahedronFilled {
 
public static int tetrahedron_filled(LinkedList<Integer> list, double water){
  int maxTetrahedrons=0; // тук ще запазим максималния брой тетраедри, които можем да напълним с вода
for(int it=0; it<list.size(); it++){ /*използваме един for цикъл, за да обходим целия
списък и същевременно да намерим обема на всеки един елемент(тетраедър) и също така
да определим колко е максималният брой тетраедри, които можем да напълним с вода
*/
double volume=((Math.sqrt(2))*(Math.pow(list.get(it),3))/(12)/(1000)); /* използваме
формулата от задача1 за намиране на обема на всеки тетраедър в списъка
*/
if(volume>water){/* ако обемът на тетраедър от списъка е по-голям от този на
количеството вода, ние го пропускаме и минаваме към следващ елемент*/
continue;
} else if(volume<water){/*в този if започваме да пълним един по един елементите от
списъка като изваждаме от максималното количество вода обема на запълнения елемент
и се връщаме в началото на цикъла, с намаленото количество вода*/
water= water-volume;
maxTetrahedrons++;
}
if(water<0){
break;
}
}
return maxTetrahedrons;
}
public static void main(String[] args) {
Scanner sca = new Scanner(System.in);
System.out.println("Enter the amount of the liters: ");
double amountWater = sca.nextDouble();
if(amountWater<=0){
System.out.println("Please enter another amount!");
return;
}
LinkedList<Integer> list1 = new LinkedList<Integer>();
Scanner sc = new Scanner(System.in);
System.out.println("Enter a positiv edge in centimeters: ");
System.out.println("If you want to exit, prease press -1");
int edge = sc.nextInt();
if((edge==0) || (edge<-1) || (edge==-1)){
System.out.println("Wrong value!");
return;
}
list1.add(edge);
while(edge!=-1){ //в един while цикъл пълним списъка с елементи
System.out.println("Enter a positiv edge in centimeters: ");
edge = sc.nextInt();
if(edge==-1){
break;
}
list1.add(edge);
}
System.out.printf("You can fill only %d "
+ " Regular tetrahedrons with %1.0f liters of water",
tetrahedron_filled(list1,amountWater),amountWater);
}
}
 
/* Забележка: променливата water е от тип double, а не от тип int.
Това се поражда от факта, че ако изпозваме int,
като изваждаме от количеството вода, обема на запълнения съд,
не можем да пресметнем точното количество вода, тъй като имаме отклонения при закръглянето и
това може да доведе до грешни резултати за максималното количество на запълнените съдове
*/
 
/* Примерен вход: 40
Примерен вход: 100,37,25,16,25,40,100,29,54
Примерен изход: 7
*/ 
