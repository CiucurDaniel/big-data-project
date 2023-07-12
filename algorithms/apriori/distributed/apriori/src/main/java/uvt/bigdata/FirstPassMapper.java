package uvt.bigdata;


import java.io.IOException;
import java.util.StringTokenizer;


import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class FirstPassMapper extends Mapper<Object, Text, Text, IntWritable> {

    private final static IntWritable one = new IntWritable(1);
    private Text item = new Text();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {

        StringTokenizer itr = new StringTokenizer(value.toString(), ",");

        while (itr.hasMoreTokens()) {
            item.set(itr.nextToken().replace(" ", ""));
            context.write(item, one);
        }
    }
}