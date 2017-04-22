import java.io.*;
import java.net.*;
import java.util.Scanner;

public class SSMCServer{
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);

		try{
			ServerSocket s = new ServerSocket(12346, 3);

			while(true){
				ClientWorker w;

				try{
					w = new ClientWorker(s.accept());
					Thread t = new Thread(w);
					t.start();
				}
				catch(IOException e){
					System.out.println("Accept error ");
					System.exit(-1);
				}
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}

class ClientWorker implements Runnable{
	private Socket client;

	ClientWorker(Socket client){
		this.client = client;
	}

	public void run(){
		
		try{
			DataInputStream din = new DataInputStream(client.getInputStream());
			int a = Integer.parseInt(din.readUTF());
			int b = Integer.parseInt(din.readUTF());

			System.out.println("The two numbers are " + a + " and " + b);
			String msg = "Sum = " + (a+b);
			System.out.println(msg);

			DataOutputStream dout = new DataOutputStream(client.getOutputStream());
			int c = a + b;
			dout.writeUTF(msg);
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}
