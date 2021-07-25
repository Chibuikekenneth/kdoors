import React from 'react'
import {Link} from 'react-router-dom'

function DoorCard(props){
    return (
        <div className="border mb-4 rounded overflow-hidden rounded-lg hover:bg-indigo-100 hover:border-transparent hover:shadow-lg">
            <div className="p-3">
                <h3 className="font-bold text-xl mb-3 mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                    <Link to={`/doors/${props.door.id}`}>
                        { props.door.name }
                    </Link>    
                </h3>
                <div className="mb-3 mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                <p className="font-bold mb-3">Address:</p>  {props.door.address.street}, {props.door.address.city}
                </div>
                <br></br>
                <div className="mb-3 mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                    <dt className="font-bold mb-3">Last Sensor Communication:</dt> 
                    <dd>{props.door.last_communication_time ? props.door.last_communication_time : 'nill'}</dd>
                </div>
                <Link 
                    to={`/doors/${props.door.id}`}
                    className="bg-green-300 text-white p-2 flex justify-center rounded-lg"
                >
                    View
                </Link>
            </div>
        </div>
    )
}

export default DoorCard