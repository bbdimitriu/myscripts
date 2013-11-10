import java.io._
import java.text._
import sys.process._

object Main extends {
    def main(args: Array[String]) {
        val moviesDir = args(0)
        val doneDir = new File(moviesDir, "done")
        if (!doneDir.mkdirs()) {
            println("Could not create 'done' directory")
        }
            
        val sdf = new SimpleDateFormat("yyyy-MM-dd")
        println("Starting compression")
        val videos = new File(moviesDir).listFiles.filter(_.getName.endsWith("MTS"))
        val modifiedDates = videos map (v => sdf.format(v.lastModified))
        var indexMap = modifiedDates.foldLeft(Map.empty[String, Int])((map, el) => map + (el -> 0))
        val fileAndDateMap = (videos map (_.getName) zip modifiedDates).toMap
        val result = fileAndDateMap map { entry =>
            val currentIdx = indexMap(entry._2)
            indexMap += (entry._2 -> (currentIdx + 1))
            if (currentIdx == 0) {
            	entry._1 -> entry._2
            } else {
                entry._1 -> (entry._2 + "-" + currentIdx)
            }
        }
	result foreach println
        // result now contains a mapping between file name and a unique date (with a suffix if necessary)
	result foreach { entry =>
            val (fileName, newName) = entry
            val toExecute = "avconv -i " + fileName + " -c:v libx264 -crf 22 -c:a libmp3lame " + newName + ".avi"
            println (toExecute)
            val status = (toExecute!)
            if (status != 0) {
                println ("Conversion for file " + fileName + " terminated with error status " + status)
            } else {
                new File(fileName).renameTo(new File(doneDir, fileName))
                println("File " + fileName + " moved to 'done' directory successfully")
            }
        }
    }
}

