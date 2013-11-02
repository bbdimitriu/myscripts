

import org.eclipse.jetty.server._
import org.eclipse.jetty.server.handler._
import javax.servlet.http.HttpServletRequest
import javax.servlet.http.HttpServletResponse
import java.io._

class HelloHandler extends AbstractHandler {
    def handle(target: String, baseRequest: Request, request: HttpServletRequest, response: HttpServletResponse) {
        response.setStatus(HttpServletResponse.SC_OK);
        if (request.getMethod().equalsIgnoreCase("POST")) {
            // read all the data and drop it
            val buffer = new Array[Byte](512)
            val noop = (a: Any) => ()
            Stream.continually(request.getInputStream().read(buffer)).takeWhile(_ != -1).foreach(noop)
        }
        baseRequest.setHandled(true);
    }
}

object JettyServer {
    def main(args: Array[String]) {
        val server = new Server(args(0).toInt)
        server.setHandler(new HelloHandler())
        server.start();
        server.join();
    }

}

