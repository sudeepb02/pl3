import java.io.*;
import java.net.*;
import java.util.Scanner;

public class SCSSClient{
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);

		try{
			Socket c = new Socket("192.168.1.110", 12345);

			System.out.println("\nEnter a message to send to server : ");

			String msg = sc.nextLine();

			DataOutputStream dout = new DataOutputStream(c.getOutputStream());
			dout.writeUTF(msg);

			DataInputStream din = new DataInputStream(c.getInputStream());
			String str = din.readUTF();

			System.out.println(str);
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}

