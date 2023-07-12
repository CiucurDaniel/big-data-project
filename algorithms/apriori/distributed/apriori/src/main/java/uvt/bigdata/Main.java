package uvt.bigdata;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class Main {
    public static void main(String[] args) throws Exception {

        int minimumSupport = Integer.parseInt(args[2]);

        for (int i = 1; i <= 4; i++) {
            Configuration conf = new Configuration();
            conf.setInt("minimumSupport", minimumSupport);
            conf.setInt("iteration", i);

            Job job = Job.getInstance(conf, "Item set iteration:" + i);
            job.setJarByClass(Main.class);

            if (i == 1) {
                job.setMapperClass(FirstPassMapper.class);
            } else {
                job.setMapperClass(KPassMapper.class);
            }

            job.setCombinerClass(IntSumReducer.class);
            job.setReducerClass(IntSumReducer.class);

            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(IntWritable.class);

            FileInputFormat.addInputPath(job, new Path(args[0]));
            FileOutputFormat.setOutputPath(job, new Path(args[1] + i));

            boolean isSuccess = job.waitForCompletion(true);
            if (!isSuccess) {
                System.err.println(i + " iteration fail");
                break;
            }
        }
    }
}