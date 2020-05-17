package Poised_Engineering;
import java.io.*;
import java.sql.SQLOutput;
import java.util.Scanner;

public class Project {

    // Attributes for a project
     int projectID;
     String projectType;
     String projectAddress;
     String projectErf;
     String projectDeadline;
     String projectName;
     String projectFee;
     String projectFeePaid;

    // all args constructor
    public Project(int projectID, String projectName, String projectType, String projectAddress, String projectErf, String projectFee, String projectFeePaid, String projectDeadline) {
        this.projectID = projectID;
        this.projectType = projectType;
        this.projectAddress = projectAddress;
        this.projectErf = projectErf;
        this.projectDeadline = projectDeadline;
        this.projectName = projectName;
        this.projectFee = projectFee;
        this.projectFeePaid = projectFeePaid;
    }

    //no args constructor
    public Project() {
    }

    // getters
    public int getProjectID() {

        Scanner input = new Scanner(System.in);
        System.out.println("Enter project number: ");
        projectID = input.nextInt();

        return projectID;
    }

    public String getProjectType() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project type: ");
        projectType = input.next();

        return projectType;
    }

    public String getProjectAddress() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project address: ");
        projectAddress = input.nextLine();

        return projectAddress;
    }

    public String getProjectErf() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project erf: ");
        projectErf = input.nextLine();

        return projectErf;
    }

    public String getProjectDeadline() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project deadline: ");
        projectDeadline = input.nextLine();

        return projectDeadline;
    }

    public String getProjectName() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project name: ");
        projectName = input.nextLine();

        return projectName;
    }

    public String getProjectFee() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project total fee: ");
        projectFee = input.nextLine();

        return projectFee;
    }

    public String getProjectFeePaid() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter project fee paid to date: ");
        projectFeePaid = input.nextLine();

        return projectFeePaid;
    }

    public String toString() {
        String output = "Project ID: " + projectID;
        output += "\nProject Name: " + projectName;
        output += "\nProject Type: " + projectType;
        output += "\nProject Address: " + projectAddress;
        output += "\nProject Erf Number: " + projectErf;
        output += "\nProject Fee: " + projectFee;
        output += "\nFees paid to date: " + projectFeePaid;
        output += "\nProject deadline: " + projectDeadline;

        return output;
    }
    // writing the new project's details to the project text file
    public void WriteToProject() throws IOException {
        try {
            FileWriter writer = new FileWriter("Projects.txt", true);
            writer.write(projectID + ",");
            writer.write(projectName + ",");
            writer.write(projectType + ",");
            writer.write(projectAddress + ",");
            writer.write(projectErf + ",");
            writer.write(projectFee + ",");
            writer.write(projectFeePaid + ",");
            writer.write(projectDeadline);
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private  Scanner x;

    public void EditDueDate(String filepath, String editProject, String dueDateNew) {
        String tempFile = "temp1.txt"; // a temporary text file used to overwrite the projects text file later
        File oldFile = new File(filepath);
        File newFile = new File(tempFile);


        try {
            FileWriter fw = new FileWriter(tempFile, true); // appending records
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw);
            Scanner x = new Scanner(new File(filepath));

            while (x.hasNext()) {   // going over all the lines in the projects file while there are lines
                String line = x.nextLine();
                String[] lineVector = line.split(",");;

                String ID = lineVector[0];  //assigning each variable
                String name = lineVector[1];
                String type = lineVector[2];
                String address = lineVector[3];
                String erfNum = lineVector[4];
                String cost = lineVector[5];
                String paid = lineVector[6];
                String date = lineVector[7];

                if (ID.equals(editProject)) { // checking if project ID matches user input, if so the entire line is written with new due date
                    pw.println(ID + "," + name + "," + type + "," + address + "," + erfNum + "," + cost + "," + paid + "," + dueDateNew);
                } else { // if not, the existing date is written
                    pw.println(ID + "," + name + "," + type + "," + address + "," + erfNum + "," + cost + "," + paid + "," + date);
                }
            }
            x.close();
            pw.flush();
            pw.close();
            oldFile.delete();
            File dump = new File(filepath);
            newFile.renameTo(dump);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void EditFeePaid(String filepath, String editProject, String feePaidNew) {
        String tempFile = "temp2.txt";
        File oldFile = new File(filepath);
        File newFile = new File(tempFile);

        try {
            FileWriter gw = new FileWriter(tempFile, true); // appending records
            BufferedWriter cw = new BufferedWriter(gw);
            PrintWriter qw = new PrintWriter(cw);
            Scanner y = new Scanner(new File(filepath));

            while (y.hasNext()) {   // going over all the lines in the projects file while there are lines
                String line = y.nextLine();
                String[] lineVector = line.split(",");;

                String ID = lineVector[0];  //assigning each variable
                String name = lineVector[1];
                String type = lineVector[2];
                String address = lineVector[3];
                String erfNum = lineVector[4];
                String cost = lineVector[5];
                String paid = lineVector[6];
                String date = lineVector[7];

                if (ID.equals(editProject)) { // checking if project ID matches user input, if so the entire line is written with new fee paid
                    qw.println(ID + "," + name + "," + type + "," + address + "," + erfNum + "," + cost + "," + feePaidNew + "," + date);


                } else { // if not, the existing fee paid is written
                    qw.println(ID + "," + name + "," + type + "," + address + "," + erfNum + "," + cost + "," + paid + "," + date);
                }
            }
            y.close();
            qw.flush();
            qw.close();
            oldFile.delete();
            File dump = new File(filepath);
            newFile.renameTo(dump);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void displayProjects(){
        try (BufferedReader br = new BufferedReader(new FileReader("Projects.txt"))) {
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



}


