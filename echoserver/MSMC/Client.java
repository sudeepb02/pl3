import java.io.*;
import java.net.*;
import java.util.*;

public class Client{
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int ch = 1;

		do{
			System.out.println(" 1.Chat Server\n 2.Add server\n 3.Exit\n");
			System.out.println("Please enter your choice : ");

			ch = sc.nextInt();

			switch(ch){
				
				case 1:
					try{
						Socket c1 = new Socket("192.168.1.110", 12345);

						System.out.println("Please enter message for server : " );
						String req = br.readLine(); 

						DataOutputStream dout = new DataOutputStream(c1.getOutputStream());
						dout.writeUTF(req);

						DataInputStream din = new DataInputStream(c1.getInputStream());
						String res = din.readUTF();

						System.out.println("Response from server : " + res);

					}
					catch(Exception e){
						e.printStackTrace();
					}
					break;

				case 2:
					try{
						Socket c2 = new Socket("192.168.1.110", 12346);

						System.out.println("Enter first number : ");
						String a = sc.next();

						System.out.println("Enter second number : ");
						String b = sc.next();

						DataOutputStream dout = new DataOutputStream(c2.getOutputStream());

						dout.writeUTF(a);
						dout.writeUTF(b);

						DataInputStream din = new DataInputStream(c2.getInputStream());
						String res = din.readUTF();

						System.out.println("Response from server :  " + res);

					}
					catch(Exception e){
						e.printStackTrace();
					}
					break;

				case 3 :
					break;
				default : 
					System.out.println("Please enter correct choice ");

			}
		}while(ch!=3);
		sc.close();
	}
}
