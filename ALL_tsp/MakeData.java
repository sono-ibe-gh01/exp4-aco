import java.io.*;

class MakeData{
    public static void main(String args[]){
        int i, ii, j=0,num=48;
        double ratio=0., X=0., Y=0., r=0. ,rr=0.;
        double[] x = new double[num];
        double[] y = new double[num];
    
        System.out.println("外円の半径を入力してください。");

    try{
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        
        String str = br.readLine();
        r = Double.parseDouble( str );
        System.out.println(r + "が入力されました。");
        System.out.println("半径比を入力してください。");
        str = br.readLine();
        ratio = Double.parseDouble( str );
        System.out.println(ratio+"が入力されました。");
    }catch (IOException e){
        System.out.println("入出力エラーです");
    }
    
    for(ii=1; ii<=4; ii++){
        for(i=15; i<=90; i+=15 ){
            X = r*Math.cos( Math.toRadians( i ) );
            Y = r*Math.sin( Math.toRadians( i ) );
        
            switch( ii ){
                case 1 :{
                    x[j] = r + X + 65;
                    y[j] = r - Y + 65;
                }break;
                case 2 :{
                    x[j] = r - Y + 65;
                    y[j] = r - X + 65;
                }break;
                case 3 :{
                    x[j] = r - X + 65;
                    y[j] = r + Y + 65;
                }break;
                case 4 :{
                    x[j] = r + Y + 65;
                    y[j] = r + X + 65;
                }break;
            }
            j++;
        }
    }
    
    rr = r * ratio;
    
    for(ii=1; ii<=4; ii++){
        for(i=15; i<=90; i+=15 ){
            X = rr*Math.cos( Math.toRadians( i ) );
            Y = rr*Math.sin( Math.toRadians( i ) );
        
            switch( ii ){
                case 1 :{
                    x[j] = r + X + 65.;
                    y[j] = r - Y + 65.;
                }break;
                case 2 :{
                    x[j] = r - Y + 65.;
                    y[j] = r - X + 65.;
                }break;
                case 3 :{
                    x[j] = r - X + 65.;
                    y[j] = r + Y + 65.;
                }break;
                case 4 :{
                    x[j] = r + Y + 65.;
                    y[j] = r + X + 65.;
                }break;
            }
            j++;
        }
    }
    try{
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(args[0])));
        
        pw.println(num);
        for(int is=0;is<num;is++){
            pw.println(x[is]);
        }
        for(int is=0;is<num;is++){
            pw.println(y[is]);
        }
        System.out.println("ファイルに書き込みました");
        pw.close();
    }catch (IOException e){
        System.out.println("入出力エラーです");
    }
    }
}