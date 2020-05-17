package Poised_Engineering;

import java.io.*;
import java.util.Scanner;

public class People {

    // Attributes
    private static int project;
     private static String type;
    private static String name;
    private static String number;
    private static String email;
    private static String address;

    // Methods
    // Constructor
    public People(int project, String type, String name, String number, String email, String address) {
        this.project = project;
        this.type = type;
        this.name = name;
        this.number = number;
        this.email = email;
        this.address = address;
    }
    //no args constructor
    public People() {
    }

    // getting the project number associated with person
    public static int getProject() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project number associated with person");
        int project = input.nextInt();

        return project;
    }

    // get type of person
    public static String getType() {
        int selection;
        Scanner input = new Scanner(System.in);
        System.out.println("Select type of person to add\n1 - Architect\n2- Contractor\n3- Customer\n ");
        selection = input.nextInt();
        if (selection == 1) {
            type = "Architect";
        } else if (selection == 2) {
            type = "Contractor";
        } else if (selection == 3) {
            type = "Customer";
        }

        return type;
    }

    // get name of person
    public static String getName() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter name of person: \n");
        name = input.nextLine();

        return name;
    }

    // get contact number of person
    public static String getNumber() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter contact number of person: \n");
        number = input.nextLine();

        return number;
    }

    // get email of person
    public static String getEmail() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter email address of person: \n");
        email = input.nextLine();

        return email;
    }

    // get address of person
    public static String getAddress() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter address of person: \n");
        address = input.nextLine();

        return address;
    }

    public String toString() {
        String output = "Project: " + project;
        output += "\nType: " + type;
        output += "\nName: " + name;
        output += "\nNumber: " + number;
        output += "\nEmail: " + email;
        output += "\nAddress: " + address;

        return output;
    }
    // method to write new person to text file
    public  void WriteToPeople() throws IOException {
        try {
            FileWriter writer = new FileWriter("People.txt", true);
            writer.write(project + ",");
            writer.write(type + ",");
            writer.write(name + ",");
            writer.write(number + ",");
            writer.write(email + ",");
            writer.write(address + "\n");
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    // to display information about people listed in people text file
    public void displayPeople(){
        try (BufferedReader br = new BufferedReader(new FileReader("People.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void EditContractorDetails(String filepath, String editProject, String numberNew, String emailNew) {
        String tempFile = "temp3.txt";
        File oldFile = new File(filepath);
        File newFile = new File(tempFile);

        try {
            FileWriter hw = new FileWriter(tempFile, true); // appending records
            BufferedWriter dw = new BufferedWriter(hw);
            PrintWriter rw = new PrintWriter(dw);
            Scanner z = new Scanner(new File(filepath));

            while (z.hasNext()) {   // going over all the lines in the projects file while there are lines
                String line = z.nextLine();
                String[] lineVector = line.split(",");;

                String ID = lineVector[0];  //assigning each variable
                String personType = lineVector[1];
                String personName = lineVector[2];
                String personNumber = lineVector[3];
                String personEmail = lineVector[4];
                String personAddress = lineVector[5];



                if (ID.equals(editProject)) { // checking if project ID matches user input, if so the entire line is written with new details on person
                    rw.println(ID + "," + personType + "," + personName + "," + numberNew + "," + emailNew + "," + personAddress);


                } else { // if not, the existing fee paid is written
                    rw.println(ID + "," + personType + "," + personName + "," + personNumber + "," + personEmail + "," + personAddress);
                }
            }
            z.close();
            rw.flush();
            rw.close();
            oldFile.delete();
            File dump = new File(filepath);
            newFile.renameTo(dump);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}