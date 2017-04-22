import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Server1{
	public static void main(String[] args){

		try{
			ServerSocket s = new ServerSocket(12345,3);

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
			String req = din.readUTF();

			System.out.println("Message from client : " + req);

			DataOutputStream dout = new DataOutputStream(client.getOutputStream());
			String res = "Hello from Server";
			dout.writeUTF(res);

		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}

