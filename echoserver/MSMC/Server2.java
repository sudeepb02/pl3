import java.io.*;
import java.util.Scanner;
import java.net.*;

public class Server2{
	public static void main(String[] args){
		
		try{
			ServerSocket s = new ServerSocket(12346, 3);

			while(true){
				
				try{
					ClientWorker w = new ClientWorker(s.accept());
					Thread t = new Thread(w);
					t.start();
				}
				catch(Exception e){
					e.printStackTrace();
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

	public void run()
	{
		try{
			DataInputStream din = new DataInputStream(client.getInputStream());
			int a = Integer.parseInt(din.readUTF());

			int b = Integer.parseInt(din.readUTF());

			int c = a + b;

			String res = "Summation of two numbers : " + c;

			DataOutputStream dout = new DataOutputStream(client.getOutputStream());
			dout.writeUTF(res);

			System.out.println(res);
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}


