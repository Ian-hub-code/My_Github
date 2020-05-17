package Poised_Engineering;

import java.io.IOException;
import java.sql.SQLOutput;
import java.util.Scanner;

public class PoisedPM {
    public static void main(String[] args) throws IOException {
        System.out.println("Poised Project Manager");
        System.out.println("----------------------");
        int selection;
        do{
            System.out.println("\n1- Create project\n2- Create person\n3- Update due date of project\n4- Edit fee paid of project\n5- Edit Contractor details\n6- Quit");
            Scanner input = new Scanner(System.in);
            selection = input.nextInt();

            if (selection == 1){
                System.out.println("--> Creating a project");
                // getting the details entered by the user for the new project
                Project p = new Project();
                int projectID = p.getProjectID();
                String pName = p.getProjectName();
                String pType = p.getProjectType();
                String projectAddress = p.getProjectAddress();
                String projectErf = p.getProjectErf();
                String projectFee = p.getProjectFee();
                String projectFeePaid = p.getProjectFeePaid();
                String projectDeadline = p.getProjectDeadline();
                // storing the new project object in n
                Project n = new Project(projectID,pName,pType,projectAddress,projectErf,projectFee,projectFeePaid,projectDeadline);

                System.out.println("Project Information");
                System.out.println("------------------");
                System.out.println(n.toString());
                System.out.println("");
                n.WriteToProject();
                System.out.println("");
                System.out.println("------------------");
                p.displayProjects();
                System.out.println("------------------");

            }
            else if (selection == 2){
                System.out.println("--> Creating a person");
                // getting the details entered by the user for the new project
                int project = People.getProject();
                String personType = People.getType();
                String personName = People.getName();
                String personNumber = People.getNumber();
                String personEmail = People.getEmail();
                String personAddress = People.getAddress();
                // storing the new person object in n, calling my write method and writing to file
                People n = new People(project,personType,personName,personNumber,personEmail,personAddress);
                System.out.println("Person Information");
                System.out.println("------------------");
                System.out.println(n.toString());
                System.out.println("");
                n.WriteToPeople();

            }
            else if (selection == 3){
                System.out.println("--> Editing due date of project");
                System.out.println("Projects listed below");
                Project p3 = new Project();
                System.out.println("");
                System.out.println("------------------");
                p3.displayProjects();
                System.out.println("------------------");
                String filepath = "Projects.txt";   // path to text file containing project details
                String editProject; // variable which will be used to get the project which I would like to edit
                String dueDateNew; // variable which will store the new due date
                System.out.println("Enter number of project which you would like to edit:");

                editProject = input.next(); // asking user to choose which project to edit due date from
                System.out.println("Enter new due date(dd/mm/yyyy):");
                dueDateNew = input.next(); // requesting new due date
                Project p = new Project();
                p.EditDueDate(filepath, editProject,dueDateNew);
                System.out.println("");
                System.out.println("------------------");
                p3.displayProjects();
                System.out.println("------------------");

            }
            else if (selection == 4){
                System.out.println("--> Editing fee paid of project");
                System.out.println("");
                System.out.println("Projects listed below");
                System.out.println("-----------------------------------------");
                Project p1 = new Project();
                p1.displayProjects();
                System.out.println("-----------------------------------------");
                String filepath = "Projects.txt";   // path to text file containing project details
                String editProject; // variable which will be used to get the project which I would like to edit
                String feePaidNew; // variable which will store the new fee paid
                System.out.println("\nEnter number of project which you would like to edit:");

                editProject = input.next(); // asking user to choose which project to edit due date from
                System.out.println("Enter new fee paid:");
                feePaidNew = input.next(); // requesting new fee paid
                Project p2 = new Project();
                p2.EditFeePaid(filepath, editProject,feePaidNew);
                System.out.println("-----------------------------------------");
                p1.displayProjects();
                System.out.println("-----------------------------------------");
            }
            else if (selection == 5){
                System.out.println("--> Editing contractor details");
                System.out.println("");
                System.out.println("People listed below");
                System.out.println("-----------------------------------------");
                People p1 = new People();
                p1.displayPeople();
                System.out.println("-----------------------------------------");
                String filepath = "People.txt";   // path to text file containing project details
                String editProject; // variable which will be used to get the project which I would like to edit
                String numberNew; // variable which will store the new number
                String emailNew;
                System.out.println("\nEnter number of project which you would like to edit:");

                editProject = input.next(); // asking user to choose which project to edit due date from
                System.out.println("Enter new number for contractor:");
                numberNew = input.next(); // requesting new fee paid
                System.out.println("Enter new email for contractor:");
                emailNew = input.next(); // requesting new fee paid
                People p2 = new People();
                p2.EditContractorDetails(filepath, editProject,numberNew, emailNew);
                System.out.println("-----------------------------------------");
                p1.displayPeople();
                System.out.println("-----------------------------------------");
            }
        }while(selection != 6);
        System.out.println("Done");
        System.exit(0);

    }

}
