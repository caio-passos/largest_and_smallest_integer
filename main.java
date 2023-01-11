import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> values = new ArrayList<Integer>();  // Create an empty list called 'values'
        Scanner scanner = new Scanner(System.in);  // Create a new Scanner object to read input from the user

        while (true) {  // infinite loop
            System.out.print("Enter a list of numbers and press enter to finish: ");
            String data = scanner.nextLine();
            if (data.length() > 0) {
                String[] numbers = data.split(" ");
                for (String number : numbers) {
                    values.add(Integer.parseInt(number));  // add the number to the 'values' list
                }
            } else {
                System.out.println("The list is: " + values);
                break;
            }
        }

        int biggest = Collections.min(values);  // find the smallest value
        int smallest = Collections.max(values); // find the biggest value
        
        System.out.println("The biggest value is: " + biggest);
        System.out.println("The smallest value is: " + smallest);
    }
}
