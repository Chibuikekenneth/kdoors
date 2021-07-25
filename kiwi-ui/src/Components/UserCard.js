import React from 'react'
import {Link} from 'react-router-dom'

function UserCard(props){
    return (
        <div className="border mb-4 rounded overflow-hidden rounded-lg hover:bg-indigo-100 hover:border-transparent hover:shadow-lg">
            <div className="p-3">
                <h3 className="text-lg leading-6 font-medium text-gray-900">
                        { props.permission.user.first_name }  { props.permission.user.last_name }    
                </h3>
                <br></br>
                <div className="mb-3 mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                <p className=" mb-3">Email: {props.permission.user.email}</p> 
                </div>
            </div>
        </div>
    )
}

export default UserCard