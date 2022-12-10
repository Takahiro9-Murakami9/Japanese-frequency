import {useEffect, useState} from "react"
import axios from "axios"
// import {format} from "date-fns"
import TextField from '@mui/material/TextField';
import './App.css';

const baseUrl = "http://localhost:5000"

function App() {
  const [description, setDescription] = useState("");
  const [getParse, setGetParse] = useState([]);
  const [eventsList, setEventsList] = useState([]);
  // const [eventId, setEventId] = useState(null);

  const fetchEvents = async () => {
    const data = await axios.get(`${baseUrl}/events`)
    const { events } = data.data
    setEventsList(events);
    // console.log("DATA: ", data)
  }

  const handleChange = e => {
    setDescription(e.target.value);
  }

  const handleGetParse = async (id) => {
    try {
      const parsedData = await axios.get(`${baseUrl}/events/${id}`);
      console.log("ParsedData: ", parsedData.data.event);
      const getParsedData = parsedData.data.event;
      console.log(getParsedData);
      setGetParse(getParsedData);
    } catch (err) {
      console.error(err.message);
    }
  }
  
  const handleDelete = async (id) => {
    try {
     await axios.delete(`${baseUrl}/events/${id}`);
     const updatedList = eventsList.filter(event => event.id !==id);
     setEventsList(updatedList);
    } catch (err) {
      console.error(err.message);
    }
  }

  // const handleEdit = (event) => {
  //   setEventId(event.id);
  //   seEditDescription(event.description);
  // }

  const handleSubmit = async(e) => {
    e.preventDefault();
    try {
      const data = await axios.post(`${baseUrl}/events`, {description})
      setEventsList([...eventsList, data.data]);
      setDescription('');
    }catch (err) {
      console.error(err.message);
    }
  }

  useEffect(() => {
    fetchEvents();
    handleGetParse();
  }, [])

  return (
    <div className="App">
      <section>
        <form onSubmit={handleSubmit}>
          <div style={{ paddingBottom: "30px" }}>
          <label htmlFor="description" >Frequency measurement</label>
          </div>
          <TextField
          className = "textfield"
          sx={{width: 500}}
          id="description"
          label="input your text"
          multiline
          maxRows={5}
          defaultValue="Default Value"
          value={description}
          onChange={handleChange}
          />
          <button type="submit" style={{ alignItems: "center" }}>Submit</button>
        </form>
      </section>
      <section>
        <ul>
          {eventsList.map(event => {
            return (
              <li style={{display: "flex"}}key={event.id}>
                {event.description}
                <button onClick={() => handleDelete(event.id)}>Delete</button>
                <button onClick={() => handleGetParse(event.id)}>Frequency</button>
              </li>
            )
          })}
          
        </ul>
      </section>
      <section>{getParse.map(each => {
        return (
          <li>{each}</li>
        )
      })}
      </section>
    </div>
  );
}

export default App;
