import java.io.*;
import java.net.*;

public class SCSSServer{
	public static void main(String[] args){
		
		try{
			ServerSocket s = new ServerSocket(12345,3);

			while(true){
				Socket sd = s.accept();

				try{
					DataInputStream dis = new DataInputStream(sd.getInputStream());
					String msg = dis.readUTF();

					System.out.println("\n Message from client is : " + msg);
					DataOutputStream dout = new DataOutputStream(sd.getOutputStream());

					String resp = "Message received by server!";
					dout.writeUTF(resp);
				}
				catch(IOException e){
					System.out.println("Error in IO");
					System.exit(-1);
				}
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
}
			
