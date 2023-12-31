package uvt.bigdata;


import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        Integer minimumSupport = context.getConfiguration().getInt("minimumSupport", 10);

        int sum = 0;

        for (IntWritable val : values) {
            sum += val.get();
        }
        result.set(sum);

        if (sum > minimumSupport) {
            System.out.println("DEBUG: Found item above min support level -> " + key.toString());
            context.write(key, result);
        }
    }
}