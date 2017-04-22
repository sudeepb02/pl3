import java.io.*;
import java.net.*;
import java.util.Scanner;

public class SSMCClient{
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);

		try{
			Socket c = new Socket("192.168.1.110",12346);

			System.out.println("Enter first number : ");
			String a = sc.next();

			System.out.println("Enter second number : ");
			String b = sc.next();

			DataOutputStream dout = new DataOutputStream(c.getOutputStream());
			dout.writeUTF(a);
			dout.writeUTF(b);

			DataInputStream din = new DataInputStream(c.getInputStream());

			String str = din.readUTF();

			System.out.println(str);
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}

