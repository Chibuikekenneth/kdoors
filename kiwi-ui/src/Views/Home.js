import React from 'react'
import Loader from '../Components/Loader'
import DoorCard from '../Components/DoorCard'
import { useAxiosGet } from '../Hooks/HttpRequests'

function Home(){
    const url = `http://localhost:5000/api/v1/doors/`
    let doors = useAxiosGet(url)

    let content = null

    if(doors.error){
        content = <div>
            <div className="bg-red-300 p-3">
                There was an error please refresh or try again later.
            </div>
        </div>
    }

    if(doors.loading){
        content = <Loader></Loader>
    }

    if(doors.data){
        content = 
        doors.data.map((door) => 
            <div key={door.id} className="flex-no-shrink w-full md:w-1/3 md:px-3">
                <DoorCard 
                    door={door}
                />
            </div>
        )
    }

    return (
        <div className="container mx-auto">
            <div className="md:flex flex-wrap md:-mx-3">
                { content } 
            </div>
        </div>
    )
}

export default Home